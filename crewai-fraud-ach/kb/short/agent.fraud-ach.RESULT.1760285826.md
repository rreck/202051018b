```json
{
  "id": "0454e6087f578109",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285826,
  "host_pid": "9e6742732c60:1",
  "hash": "0a941b1263ed192249d4a4d79f306703196a53b0a758e9b1b96256bdf77479f6",
  "cid": "QmV10a941b1263ed192249d4a4d79f306703196a53b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285826,
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
      "evaluated_at": 1760285826
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
  "sig": "7f304edb52f3c90877b4972f87bcc0a3b1fb9cc1a08e93fd1f5431f4c157d779"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201460464182
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285765, 'matching_hash': '97f231b14306ced8'}}}