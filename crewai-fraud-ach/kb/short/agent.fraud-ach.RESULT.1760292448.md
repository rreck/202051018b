```json
{
  "id": "62c24cc724330275",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292448,
  "host_pid": "9e6742732c60:1",
  "hash": "a230e4f31ae277b0babfe0f9d59e4e27a47948fa1974aa4cc4d59c981726bfce",
  "cid": "QmV1a230e4f31ae277b0babfe0f9d59e4e27a47948fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292448,
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
      "evaluated_at": 1760292448
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
  "sig": "d37b160d50143146b171979ba6f7626419712acb994b0aa0311b2268775b86cc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591082294
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 91963278, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285763, 'matching_hash': 'b890dc886075e9be'}}}