```json
{
  "id": "b880c8a37b35d85c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288408,
  "host_pid": "9e6742732c60:1",
  "hash": "215be540a6a2ceb071195bd77df31ed60fb2323d8ae26a53e98132d058cdbc95",
  "cid": "QmV1215be540a6a2ceb071195bd77df31ed60fb2323d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288408,
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
      "evaluated_at": 1760288408
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
  "sig": "78bbd07a9c2090d8e01d6422f8543b252f29dd25d05e0ebe88fde5f165b0d27c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590866940
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 39099632, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285765, 'matching_hash': '66ff896a34603a53'}}}