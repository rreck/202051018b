```json
{
  "id": "4a7a3cd31d6e2789",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289433,
  "host_pid": "9e6742732c60:1",
  "hash": "7b9852cf7d6e8e78b3fce05402f667166108cc4637f60b6a2a02780ebb5ca4c6",
  "cid": "QmV17b9852cf7d6e8e78b3fce05402f667166108cc46",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289433,
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
      "evaluated_at": 1760289433
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
  "sig": "71258739bfd84a8eb2987f576963a4a502b7d7cc744d1efeb610f8576defebbc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201468543646
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 58174695, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285763, 'matching_hash': '526960b6a0cd6e16'}}}