```json
{
  "id": "7bfb47490b947d79",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289222,
  "host_pid": "9e6742732c60:1",
  "hash": "d5c2d65966b0b2b7857a5038b46fd4d3c9717fef14bef760bf21da5b38f07d0f",
  "cid": "QmV1d5c2d65966b0b2b7857a5038b46fd4d3c9717fef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289222,
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
      "evaluated_at": 1760289222
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
  "sig": "7f5d4562d3a6cb74a364728d92f1e465b0565709b83ed6b252c3a09ce4637684"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021988031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 117, 'threshold': 50, 'total_amount': 29585439, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 116, 'first_seen': 1760285764, 'matching_hash': '88465ad333807d91'}}}