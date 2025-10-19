```json
{
  "id": "ab4e395a45c579cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292778,
  "host_pid": "9e6742732c60:1",
  "hash": "78259477109c0385aaea3110dd961952c00001b4e1f0ce9bfd8d6d56c1a0ef2b",
  "cid": "QmV178259477109c0385aaea3110dd961952c00001b4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292778,
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
      "evaluated_at": 1760292778
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
  "sig": "9ba1773e1c15231b3546c022312ee0d85e94901a5560b15ac262370470a17005"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025759024
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 78459855, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285763, 'matching_hash': 'fa026da4c6071776'}}}