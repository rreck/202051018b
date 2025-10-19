```json
{
  "id": "709b7c16151266f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292856,
  "host_pid": "9e6742732c60:1",
  "hash": "07fd95cd2b147f6eb23691039318346f0d82f68cde1913ffa3c3c92cbc6a4265",
  "cid": "QmV107fd95cd2b147f6eb23691039318346f0d82f68c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292856,
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
      "evaluated_at": 1760292856
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
  "sig": "43e798b548fb76d48044911957fab27775f469aeb792755d4806c445ee250490"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467961793
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 13803442, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285765, 'matching_hash': '7ef856857e97207f'}}}