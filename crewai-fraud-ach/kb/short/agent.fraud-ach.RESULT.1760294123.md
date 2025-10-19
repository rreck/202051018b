```json
{
  "id": "4a2271fd1eb40dec",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294123,
  "host_pid": "9e6742732c60:1",
  "hash": "174088626fd246e6807904e393074e6e3556909f8bb1d0714db594b5fa63a800",
  "cid": "QmV1174088626fd246e6807904e393074e6e3556909f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294123,
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
      "evaluated_at": 1760294123
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
  "sig": "08c60f009940290e5883a0881a8f6bd56c93a880ba4808c602d472aca94c6714"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596363200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 88558576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285764, 'matching_hash': 'b9f8fedd6c477a32'}}}