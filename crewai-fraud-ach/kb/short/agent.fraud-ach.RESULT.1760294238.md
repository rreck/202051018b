```json
{
  "id": "1960f0db2851d894",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294238,
  "host_pid": "9e6742732c60:1",
  "hash": "773b4941ed558499dcd2190e0be28883f83ed5fd6c5bd19558e89deef5be0327",
  "cid": "QmV1773b4941ed558499dcd2190e0be28883f83ed5fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294238,
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
      "evaluated_at": 1760294238
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
  "sig": "e945fb9ede3c9ea7e1dd43dcd76830edbfe46fc1cbd6bbc24018ee18fc7f95fc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464924143
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 310, 'threshold': 50, 'total_amount': 125979350, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 309, 'first_seen': 1760284979, 'matching_hash': '7b94effc1b7c4489'}}}