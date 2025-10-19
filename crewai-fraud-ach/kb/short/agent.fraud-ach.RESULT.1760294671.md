```json
{
  "id": "dc23158ea682b38d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294671,
  "host_pid": "9e6742732c60:1",
  "hash": "7770a8d87bccf5050a544c64557c9304f8d9190c4c3e35a4882cfac7ceaaa9cf",
  "cid": "QmV17770a8d87bccf5050a544c64557c9304f8d9190c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294671,
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
      "evaluated_at": 1760294671
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
  "sig": "04213f8da32281cb08475c027986394ef1bde946512fecb9dc9f03d39720ffae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037578651
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 242, 'threshold': 50, 'total_amount': 19577074, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 241, 'first_seen': 1760285763, 'matching_hash': '25cb229761d99325'}}}