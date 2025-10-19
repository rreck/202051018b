```json
{
  "id": "360532891514f5be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289367,
  "host_pid": "9e6742732c60:1",
  "hash": "40fd920a8c0fbe3cdf33bacaa29fed6ba11100a7b41c795cd8017f9b523a7f4d",
  "cid": "QmV140fd920a8c0fbe3cdf33bacaa29fed6ba11100a7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289367,
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
      "evaluated_at": 1760289367
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
  "sig": "700ae2afe30f97097dac5dbf75567e57ba1f17b05400c9b767351c4162ef2523"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595235556
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 121, 'threshold': 50, 'total_amount': 21122486, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 120, 'first_seen': 1760285765, 'matching_hash': 'e45b9dbcffb11ba0'}}}