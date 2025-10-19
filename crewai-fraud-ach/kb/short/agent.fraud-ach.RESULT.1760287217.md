```json
{
  "id": "c77e465f7826c0d2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287217,
  "host_pid": "9e6742732c60:1",
  "hash": "406a0c88a1224c7b958160ad2f847325743d53030a1f14ab346b70faea46d61a",
  "cid": "QmV1406a0c88a1224c7b958160ad2f847325743d5303",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287217,
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
      "evaluated_at": 1760287217
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "159d9b60150b2ec609e882e89f26f7670b6a5d453646eb131e4dd09778d6c257"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105153371756
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 52, 'threshold': 50, 'total_amount': 21711560, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 51, 'first_seen': 1760285764, 'matching_hash': 'f6b71775dc53ea2e'}}}