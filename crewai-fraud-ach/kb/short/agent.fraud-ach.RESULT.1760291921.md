```json
{
  "id": "e2298cdd9620ef0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291921,
  "host_pid": "9e6742732c60:1",
  "hash": "61895b6da114233cfd1e038150d00eb67e552d7fc38e448f4f8fc17d31900917",
  "cid": "QmV161895b6da114233cfd1e038150d00eb67e552d7f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291921,
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
      "evaluated_at": 1760291921
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
  "sig": "f2821144e155f8ac9bc5a2e1afa67469803f68f91b3ad81e50c65655dae87b5a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242680908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 186, 'threshold': 50, 'total_amount': 64124988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 185, 'first_seen': 1760285764, 'matching_hash': '8e78dc9e18bacaa7'}}}