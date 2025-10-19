```json
{
  "id": "428256232b645a7c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290892,
  "host_pid": "9e6742732c60:1",
  "hash": "349c0772b8f3742eef98770254f0e8680c4af905ddb8772dd3f18142de577e3b",
  "cid": "QmV1349c0772b8f3742eef98770254f0e8680c4af905",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290892,
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
      "evaluated_at": 1760290892
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
  "sig": "e2cd57ed48d483414c66df33f28972a02c4cd202c6e697cf8684cbfe697489d0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021760547
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 42025878, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': 'fad63ed6e9f4a51a'}}}