```json
{
  "id": "f0c07935beae9e08",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292332,
  "host_pid": "9e6742732c60:1",
  "hash": "4448c757b9d57260c5ac48c37c2b3908cea88d903cb507874d59463dff1df8f9",
  "cid": "QmV14448c757b9d57260c5ac48c37c2b3908cea88d90",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292332,
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
      "evaluated_at": 1760292332
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
  "sig": "9a996673b786a23c1789485aee0f6a40e88c2f141a80861bb3747e7c3ad34615"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021533630
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 195, 'threshold': 50, 'total_amount': 28745730, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 194, 'first_seen': 1760285765, 'matching_hash': 'e04be99e47eedc93'}}}