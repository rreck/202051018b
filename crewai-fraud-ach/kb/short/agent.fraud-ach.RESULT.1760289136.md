```json
{
  "id": "4b862dba4df2f904",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289136,
  "host_pid": "9e6742732c60:1",
  "hash": "3c866deb30ada4b48c9311e818f6cbeb4276c3db493b9e064a1eb695d73795bb",
  "cid": "QmV13c866deb30ada4b48c9311e818f6cbeb4276c3db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289136,
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
      "evaluated_at": 1760289136
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
  "sig": "a84db9145f5a12d227bcbaefef1e60265d9e219cc3eafbb47f7f994a2c734f07"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025198728
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 10697532, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285765, 'matching_hash': 'ff4b51392b1a88ca'}}}