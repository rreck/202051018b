```json
{
  "id": "dede5051e4165b6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294886,
  "host_pid": "9e6742732c60:1",
  "hash": "fa56216b41470da23dba94fe11d4abe27dc34ab2f063ec00257f2dc8539aa323",
  "cid": "QmV1fa56216b41470da23dba94fe11d4abe27dc34ab2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294886,
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
      "evaluated_at": 1760294886
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
  "sig": "7e8a52da50e4a84a2744efb1ca86bfb8f58d7ad602048290a72fc4fb8851e04a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000024460145
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 62387322, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285763, 'matching_hash': '6128e7e8f1f7694a'}}}