```json
{
  "id": "cf50950b898b2a5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288217,
  "host_pid": "9e6742732c60:1",
  "hash": "744fda8e72be8abd0e323031194a377675042c11014b685250ea6ba6882e3a77",
  "cid": "QmV1744fda8e72be8abd0e323031194a377675042c11",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288217,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760288217
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "dff43949d12639c444f459943612c53838346e953fb1fc9704a2aea54ba85a92"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248914863
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285765, 'matching_hash': '9c0338b7ffb65590'}}}