```json
{
  "id": "dcf5c214aaf3308f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290481,
  "host_pid": "9e6742732c60:1",
  "hash": "7164a3f52fa616b2db317a780ae865544380f804ae8822e90979c9c81aa09a4d",
  "cid": "QmV17164a3f52fa616b2db317a780ae865544380f804",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290481,
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
      "evaluated_at": 1760290481
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
  "sig": "68cad8dfebc0dff02ce719197852d32ce3b4f497ba27308f2b84c20624c2077d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590866940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 64174396, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}