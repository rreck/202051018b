```json
{
  "id": "c3cc3c44c59b52d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289332,
  "host_pid": "9e6742732c60:1",
  "hash": "43a4dea5fbc9fc8c9caf051bd93b8d2772b72a5e580f9460d6fe5c36fa921919",
  "cid": "QmV143a4dea5fbc9fc8c9caf051bd93b8d2772b72a5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289332,
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
      "evaluated_at": 1760289332
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
  "sig": "28301687b5b62973cfd4492cd95ba59692dcd18327f5db899f129b00fe8f4143"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596790322
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 196, 'threshold': 50, 'total_amount': 10257464, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 195, 'first_seen': 1760284979, 'matching_hash': 'b9497544c8340a37'}}}