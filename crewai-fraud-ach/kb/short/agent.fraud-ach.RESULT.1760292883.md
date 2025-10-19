```json
{
  "id": "f19148fb1b117de1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292883,
  "host_pid": "9e6742732c60:1",
  "hash": "ec3d6146c016c916609e0ff69e8b15930f34e6df57f6c9ed865cff0852dd3e6a",
  "cid": "QmV1ec3d6146c016c916609e0ff69e8b15930f34e6df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292883,
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
      "evaluated_at": 1760292883
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
  "sig": "6e359dcf8d043540d84521c415484e0924f642e14b4727ed08b6017cc53fd1ef"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241012804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 57163050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'ba9ba43773b08e05'}}}