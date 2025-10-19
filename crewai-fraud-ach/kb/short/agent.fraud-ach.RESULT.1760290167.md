```json
{
  "id": "853aad51da606bd3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290167,
  "host_pid": "9e6742732c60:1",
  "hash": "e8ab9d486919a1df42a23ef4896bba5aad38607d4a56becbf042f288b8efa690",
  "cid": "QmV1e8ab9d486919a1df42a23ef4896bba5aad38607d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290167,
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
      "evaluated_at": 1760290167
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
  "sig": "1cc212b72d67de681d9ee15705f326b1cf4f828556d4de434be12baa6d8211b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009598847454
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 49585536, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': '71a427f0fcb5a05e'}}}