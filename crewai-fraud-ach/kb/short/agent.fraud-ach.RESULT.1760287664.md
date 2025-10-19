```json
{
  "id": "c8b69a217928972c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287664,
  "host_pid": "9e6742732c60:1",
  "hash": "276bef611ba3dd6f7be30f040b4f84549b5cd2c2f5e07949e5b7b7182c9eb27f",
  "cid": "QmV1276bef611ba3dd6f7be30f040b4f84549b5cd2c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287664,
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
      "evaluated_at": 1760287664
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
  "sig": "e9178f33712fed6063ad8304edf6cf432d16f597b78f18641a1836e16d87bd16"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463621906
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 22993248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285763, 'matching_hash': 'c1b23d91813533f7'}}}