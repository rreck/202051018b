```json
{
  "id": "82e494affe5dff4b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288079,
  "host_pid": "9e6742732c60:1",
  "hash": "5e5b0ca26dd92f67b5b1f27826c1813aeaa64e87c6f58eb094d4fd3b337c2ff5",
  "cid": "QmV15e5b0ca26dd92f67b5b1f27826c1813aeaa64e87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288079,
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
      "evaluated_at": 1760288079
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
  "sig": "478991fc83b3560f4a61a840b472a4b913632379e8c00baa79e8716d8926ac29"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247065619
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 32789094, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285763, 'matching_hash': '73a93f9011d99735'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 1000000}}}