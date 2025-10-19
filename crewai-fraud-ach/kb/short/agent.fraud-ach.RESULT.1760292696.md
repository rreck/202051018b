```json
{
  "id": "9e38e6146e759a35",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292696,
  "host_pid": "9e6742732c60:1",
  "hash": "3cbe6443dd7e419cc5a59972b7a11dcd06514d824f614d93d732d25d84652b4e",
  "cid": "QmV13cbe6443dd7e419cc5a59972b7a11dcd06514d82",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292696,
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
      "evaluated_at": 1760292696
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
  "sig": "dfdf3ed8f3634c9f0a96cbd0950657106a3292c687fca9515aee0ea0c791ff35"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590136300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 100571681, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285764, 'matching_hash': '2d6fc2065b3c1287'}}}