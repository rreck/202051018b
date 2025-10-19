```json
{
  "id": "ac5bb59e6a35288c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293513,
  "host_pid": "9e6742732c60:1",
  "hash": "c4156ef8bf97cda5a14f1e83c4690f78e17f0da953520dd251e4727340e36c2b",
  "cid": "QmV1c4156ef8bf97cda5a14f1e83c4690f78e17f0da9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293513,
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
      "evaluated_at": 1760293513
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
  "sig": "f4d43897b14897f9ef93586478843478e89f19f06afb18af36a313e7a1184d78"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591602283
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 32016820, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285763, 'matching_hash': '995d19d96715feaf'}}}