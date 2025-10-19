```json
{
  "id": "da9f135634df910f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293976,
  "host_pid": "9e6742732c60:1",
  "hash": "34f537e2ecb5da8bf3f5c10282f272d2dce8cf6202e794b2822ad7e650170dc9",
  "cid": "QmV134f537e2ecb5da8bf3f5c10282f272d2dce8cf62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293976,
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
      "evaluated_at": 1760293976
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
  "sig": "e46ef04aa6adfb14e55883f59ab4937433f4827c1cc9e5af4377b15114c24583"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278705813
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 229, 'threshold': 50, 'total_amount': 72077521, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 228, 'first_seen': 1760285764, 'matching_hash': '628aaca406e38baa'}}}}