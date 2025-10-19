```json
{
  "id": "d53571314a80fa61",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293284,
  "host_pid": "9e6742732c60:1",
  "hash": "7118e42c91abcac100382311ae4d2980b1d430c597f8758c42adadbc5472a073",
  "cid": "QmV17118e42c91abcac100382311ae4d2980b1d430c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293284,
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
      "evaluated_at": 1760293284
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
  "sig": "14fbd417dba4bc73fb015e75b592e6df8b67ab4c0dfa376751f1b5a5508592e2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243649474
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 75860600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285763, 'matching_hash': '901672e1b111b3e4'}}}