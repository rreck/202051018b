```json
{
  "id": "c011b0b37f688960",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291321,
  "host_pid": "9e6742732c60:1",
  "hash": "ca910567fab0e6fc0fb31793bf6479badae2ccb8c0a131d8280b9d6d62d1005d",
  "cid": "QmV1ca910567fab0e6fc0fb31793bf6479badae2ccb8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291321,
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
      "evaluated_at": 1760291321
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
  "sig": "724ee166671cccc9177d704fb3931cb85c16c54ead3117454551faaab9416b1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242027891
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 24003460, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285764, 'matching_hash': '176f574fbb51fea2'}}}}