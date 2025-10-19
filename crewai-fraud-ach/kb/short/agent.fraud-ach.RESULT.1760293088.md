```json
{
  "id": "4d4b1df5337d522b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293088,
  "host_pid": "9e6742732c60:1",
  "hash": "e01c26333dfb9e46bdfa7b37ba61c34ec67dd704dc34f83e04c9e38673dbb9a9",
  "cid": "QmV1e01c26333dfb9e46bdfa7b37ba61c34ec67dd704",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293088,
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
      "evaluated_at": 1760293088
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
  "sig": "919dd8bf94f4176f63c56532983fd906806c3fd447c70b821b495f5ebba3f8ad"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 287, 'threshold': 50, 'total_amount': 120940078, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 286, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}