```json
{
  "id": "46f047abef09ceb0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287179,
  "host_pid": "9e6742732c60:1",
  "hash": "84951b2d2afa16fb289482fd4017e7e3753a2dc2063defc10d42c047cd724d0a",
  "cid": "QmV184951b2d2afa16fb289482fd4017e7e3753a2dc2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287179,
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
      "evaluated_at": 1760287179
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "0a056892fd82f5414fcd0327842f2a9160ff41ea4137fcc47eb176537eebcf43"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009599855850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 18441294, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285763, 'matching_hash': 'c589ba109b80fe94'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '013419643', 'validation_error': 'Invalid routing number checksum'}}}