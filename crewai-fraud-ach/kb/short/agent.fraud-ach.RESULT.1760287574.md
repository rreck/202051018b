```json
{
  "id": "c7a712029355f7a7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287574,
  "host_pid": "9e6742732c60:1",
  "hash": "114916bb9b430a0ca2fa2f0b458e23879cd7fb145aaf87da7211ba8021734ba1",
  "cid": "QmV1114916bb9b430a0ca2fa2f0b458e23879cd7fb14",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287574,
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
      "evaluated_at": 1760287574
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
  "sig": "1582bb59503c50a901aa78cda3f5ded90356f552eedfdebbfc659799d0fdd32c"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 021000028116675
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50, 'total_amount': 22125675, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285763, 'matching_hash': '276303153292771e'}}}