```json
{
  "id": "c08a0f666a5dc3c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288029,
  "host_pid": "9e6742732c60:1",
  "hash": "aa1b6ef1cf3b325bed2680cce992791ac459cccba553f17220851d37bb54ba6a",
  "cid": "QmV1aa1b6ef1cf3b325bed2680cce992791ac459cccb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288029,
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
      "evaluated_at": 1760288029
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
  "sig": "df1ba7f372d867685dec3f5c41afc7e4042a137db977f56f6830657be5667b0b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469103825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 28943120, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285764, 'matching_hash': 'e83bf56ea8077a45'}}}