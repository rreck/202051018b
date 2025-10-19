```json
{
  "id": "62ff45db7dafc1c2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289049,
  "host_pid": "9e6742732c60:1",
  "hash": "c1790e5c04fedd50335d55a386d38e51bae3aaec3058e9cf90931216bd174f17",
  "cid": "QmV1c1790e5c04fedd50335d55a386d38e51bae3aaec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289049,
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
      "evaluated_at": 1760289049
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
  "sig": "0088946dc39640def29b48822afdcf12cd34b50105461d30000060fca866397b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466882033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 112, 'threshold': 50, 'total_amount': 33553184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 111, 'first_seen': 1760285763, 'matching_hash': '7e4548b1f8f2bba3'}}}