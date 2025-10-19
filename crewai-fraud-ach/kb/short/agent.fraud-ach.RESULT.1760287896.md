```json
{
  "id": "ad97370efb58d431",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287896,
  "host_pid": "9e6742732c60:1",
  "hash": "1f0ce55656eafc2639d048671d79118af6675792ab1d1bb360db51cee0e71356",
  "cid": "QmV11f0ce55656eafc2639d048671d79118af6675792",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287896,
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
      "evaluated_at": 1760287896
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
  "sig": "f5ca98e31c596ba30101c2603d1a710339d1f1ce2cf83072081abb06efefc0e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243028505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285763, 'matching_hash': '47e30fe250bb416c'}}}