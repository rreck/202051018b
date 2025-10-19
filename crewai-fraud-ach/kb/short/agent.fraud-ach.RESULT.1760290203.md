```json
{
  "id": "67da2e8bf9c443c7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290203,
  "host_pid": "9e6742732c60:1",
  "hash": "efb081457739355d6dea31885bc605cb3f7b2e0995385693125ef9f8aae1b191",
  "cid": "QmV1efb081457739355d6dea31885bc605cb3f7b2e09",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290203,
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
      "evaluated_at": 1760290203
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
  "sig": "b1cdf8afc85e0c1d2d8893a1aaaf8a2f30a26873d545707445f0927d0256b337"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155376461
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 43328304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285765, 'matching_hash': 'ed3a1cd9da35e724'}}}