```json
{
  "id": "c1243d101a1e62b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288731,
  "host_pid": "9e6742732c60:1",
  "hash": "f2f2e8a8ddd0b934a979c820803b46c1d623b2a55c4f06f54a89b9189d0a8227",
  "cid": "QmV1f2f2e8a8ddd0b934a979c820803b46c1d623b2a5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288731,
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
      "evaluated_at": 1760288731
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
  "sig": "c9402fc20cde7f9690d3eabbf2fb290845c044e292f790cab8a599d9ae0f7e06"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021053905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 25955940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285764, 'matching_hash': '608646e34fdf4d5c'}}}