```json
{
  "id": "ce17e941464e0f1d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289554,
  "host_pid": "9e6742732c60:1",
  "hash": "c17b889e573a55f1c4e3e0acbf79b3b7f2c9323f9a396bc2d2de479e41fff619",
  "cid": "QmV1c17b889e573a55f1c4e3e0acbf79b3b7f2c9323f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289554,
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
      "evaluated_at": 1760289554
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
  "sig": "b355e498f2309736ce319216d0eddacf3f17fa79a734ed31c9d655f50d504f4b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 126, 'threshold': 50, 'total_amount': 40099248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 125, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}