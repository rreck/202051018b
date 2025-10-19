```json
{
  "id": "0c0e1dd69e2850e1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289550,
  "host_pid": "9e6742732c60:1",
  "hash": "bb8af20fa9dfd6bc5dccd65d2dd7d99da458281dcbd8bb014a21bb904a4a10cb",
  "cid": "QmV1bb8af20fa9dfd6bc5dccd65d2dd7d99da458281d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289550,
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
      "evaluated_at": 1760289550
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
  "sig": "4f702a54a75612cf6255c2ae233a92f7c07027ae085a268c3d61a5da81935b36"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463882943
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 15625008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}