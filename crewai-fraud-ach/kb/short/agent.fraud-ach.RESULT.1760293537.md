```json
{
  "id": "aafeeaac24f93e5e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293537,
  "host_pid": "9e6742732c60:1",
  "hash": "d2dba4e97e94eef5501173abe7e6181c9f458681e8729339f2626d60799674bc",
  "cid": "QmV1d2dba4e97e94eef5501173abe7e6181c9f458681",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293537,
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
      "evaluated_at": 1760293537
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
  "sig": "220d9c2741ca84cbf49af1ddc51cbf5b6762072fa0a95c8b96ce78a701f06229"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466702370
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 29412680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285765, 'matching_hash': 'c2e86be7e57e9a06'}}}