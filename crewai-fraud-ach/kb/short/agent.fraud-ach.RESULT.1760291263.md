```json
{
  "id": "b2f4c7b8196f5e9f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291263,
  "host_pid": "9e6742732c60:1",
  "hash": "26f4234fefbaa0eb72c40183474fc3db2a1420bc428a0767584050c27622e49d",
  "cid": "QmV126f4234fefbaa0eb72c40183474fc3db2a1420bc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291263,
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
      "evaluated_at": 1760291263
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
  "sig": "c42de66c15381003437c392b1410389769ff0817804a618c7aacd1f2fc6af8b0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025560621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 46450440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285763, 'matching_hash': '1e88fa5a655ec1c9'}}}