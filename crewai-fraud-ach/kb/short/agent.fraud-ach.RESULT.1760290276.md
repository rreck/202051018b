```json
{
  "id": "15e4d11573e6f21b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290276,
  "host_pid": "9e6742732c60:1",
  "hash": "9aaa61b4ac7476b88b3d18aa85e34ed25dfee5f28a2fe3ae78e24144ec2c25d5",
  "cid": "QmV19aaa61b4ac7476b88b3d18aa85e34ed25dfee5f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290276,
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
      "evaluated_at": 1760290276
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
  "sig": "8bb0015e020a0ce60df85fb7cd8f9779fe18cdcffd5069dc310382ddadf9bfa0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026682072
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 49081550, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285764, 'matching_hash': 'ef2983ea6f6c1303'}}}