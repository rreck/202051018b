```json
{
  "id": "7d2114efb3ccf387",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293404,
  "host_pid": "9e6742732c60:1",
  "hash": "e64d7817cf90eec9c080f1ae304f9738600db99bb8a2eedf1b1183c6900f1392",
  "cid": "QmV1e64d7817cf90eec9c080f1ae304f9738600db99b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293404,
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
      "evaluated_at": 1760293404
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
  "sig": "6a9ef587b8b22f94c345d09abf31e0e69f22239ab97716c9a43a783a2dcb9189"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271879965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 46237582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': '9c4837aa9a8e4a4a'}}}