```json
{
  "id": "7e6b485c6bbb1a72",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293810,
  "host_pid": "9e6742732c60:1",
  "hash": "70632ea82ecafbf842fe567d0475b05b64d8fc131b0dd19d673ae84bde9840b3",
  "cid": "QmV170632ea82ecafbf842fe567d0475b05b64d8fc13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293810,
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
      "evaluated_at": 1760293810
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
  "sig": "ace193c83fb982ca48907dd8d68022995cb6fefee475a12dfc8b58897abcc6f6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024762963
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 22600000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285764, 'matching_hash': 'dd3a0eba0797b423'}}}