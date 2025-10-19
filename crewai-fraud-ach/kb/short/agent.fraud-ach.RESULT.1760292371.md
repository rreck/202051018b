```json
{
  "id": "019a831dbe5100df",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292371,
  "host_pid": "9e6742732c60:1",
  "hash": "ae3d9c79d893c2d962d0ba0aa9576fe4e488394ff4da89d2a2d2fb5466c0f250",
  "cid": "QmV1ae3d9c79d893c2d962d0ba0aa9576fe4e488394f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292371,
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
      "evaluated_at": 1760292371
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
  "sig": "1902cd814e9d9460cdfb353c74dcf0b8c3d2df04def66f86c23c4b1c9747e494"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242647259
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 51560544, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760285763, 'matching_hash': '186ae6e653ee56a6'}}}