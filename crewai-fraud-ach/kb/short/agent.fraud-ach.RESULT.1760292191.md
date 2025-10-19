```json
{
  "id": "aba9507d3347aa50",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292191,
  "host_pid": "9e6742732c60:1",
  "hash": "da1d83dd0ec0fb67a312451fc4b8b0669b567bbc7d8640be3c81e6acc93a932d",
  "cid": "QmV1da1d83dd0ec0fb67a312451fc4b8b0669b567bbc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292191,
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
      "evaluated_at": 1760292191
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
  "sig": "412188aa3fa61c47a03019f9a164abdb1e7a848bff48192035a16a63006fc8d7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028413829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 29703936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285763, 'matching_hash': '35164be796d7e820'}}}