```json
{
  "id": "5d61d4e65257d517",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292651,
  "host_pid": "9e6742732c60:1",
  "hash": "5d7022aa6fbdc3a874987c4ea388c031c5b98c2ffd687bf5eb5d187c2fc9a059",
  "cid": "QmV15d7022aa6fbdc3a874987c4ea388c031c5b98c2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292651,
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
      "evaluated_at": 1760292651
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
  "sig": "548dc7af44731215511c61b4285c4f2c5a3e7f2814f226e3e7ea286ba77fe56a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248226164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 58888656, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285763, 'matching_hash': 'b7846971abb7164d'}}}