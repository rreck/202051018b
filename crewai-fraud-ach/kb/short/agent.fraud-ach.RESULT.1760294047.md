```json
{
  "id": "5e7f3a3bff4f17ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294047,
  "host_pid": "9e6742732c60:1",
  "hash": "7adacfa4c845738b02c9978a03124f16b2cb936c292a841a859de70b96945ba8",
  "cid": "QmV17adacfa4c845738b02c9978a03124f16b2cb936c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294047,
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
      "evaluated_at": 1760294047
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
  "sig": "7aab767da0002c6e0611cecb970cc1069b9b16003e942078a4d08ec11a9719f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029386599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 19337480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}