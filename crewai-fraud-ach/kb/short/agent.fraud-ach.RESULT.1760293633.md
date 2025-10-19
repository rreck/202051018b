```json
{
  "id": "55c1adf4f1b3532c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293633,
  "host_pid": "9e6742732c60:1",
  "hash": "1362707a269d40bdb1585268ef4b586c8f6bec2ba741ba0dac7a27c9948b7d2b",
  "cid": "QmV11362707a269d40bdb1585268ef4b586c8f6bec2b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293633,
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
      "evaluated_at": 1760293633
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
  "sig": "088ce3f625581785a2664ce6a46e7dba74748ee58b0d693b40766b73320bb524"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245911336
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 110508492, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285765, 'matching_hash': '6e0081c3975eda61'}}}