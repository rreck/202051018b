```json
{
  "id": "d97520d7a60d3c48",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289305,
  "host_pid": "9e6742732c60:1",
  "hash": "664e1cbf4b49a244819e6c31d70357e89a78ffa800cb6a5123ad87ff8f9b7d47",
  "cid": "QmV1664e1cbf4b49a244819e6c31d70357e89a78ffa8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289305,
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
      "evaluated_at": 1760289305
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
  "sig": "2177453f6920e73d74e8575c457f8aacf942f64471f02325fbf03f7a9ff150d5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274578801
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 119, 'threshold': 50, 'total_amount': 20901160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 118, 'first_seen': 1760285765, 'matching_hash': 'c58645b7bcecdbfd'}}}