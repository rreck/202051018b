```json
{
  "id": "09787e29e1ca58ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287194,
  "host_pid": "9e6742732c60:1",
  "hash": "5b1730e8f2398a0423fee97353baa8bc3107d3fa8174d0759e176b4616ac6983",
  "cid": "QmV15b1730e8f2398a0423fee97353baa8bc3107d3fa",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287194,
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
      "evaluated_at": 1760287194
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "2b1ccef195fb1e52a3b05ae8297a252a288959c6e356f58fa7f2dcf2e326377d"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000023496704
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 17291703, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285765, 'matching_hash': 'f379baac52e28232'}}}