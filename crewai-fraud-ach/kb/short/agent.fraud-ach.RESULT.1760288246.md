```json
{
  "id": "65910423a3d95751",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288246,
  "host_pid": "9e6742732c60:1",
  "hash": "31717f0de7ede9facfd5464f4ad7e8f5c51e63d7910c6970371c037ed3dc57d4",
  "cid": "QmV131717f0de7ede9facfd5464f4ad7e8f5c51e63d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288246,
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
      "evaluated_at": 1760288246
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
  "sig": "8ba5e8ce8d7eb88312c2f43da29be0a64990253f4cdae6f37739fa52fc10fd59"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000036717829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 87, 'threshold': 50, 'total_amount': 15028293, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 86, 'first_seen': 1760285764, 'matching_hash': '49d069f76f563267'}}}