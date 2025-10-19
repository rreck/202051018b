```json
{
  "id": "01c331c4be4317c0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287663,
  "host_pid": "9e6742732c60:1",
  "hash": "411881f5ffcc65d1525a5c3f408fd439d04d75b61aad186d8783e9280049fe78",
  "cid": "QmV1411881f5ffcc65d1525a5c3f408fd439d04d75b6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287663,
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
      "evaluated_at": 1760287663
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
  "sig": "88a0c47d8320a40b7bd18a016c692ff9bc3ac112497c78abd18497baabda59c2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000025012070
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285763, 'matching_hash': '924eab78eaf0d48b'}}}een': 1760285763, 'matching_hash': '5102e2097242c74b'}}}