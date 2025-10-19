```json
{
  "id": "2b66bfb43f2c9ce8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291230,
  "host_pid": "9e6742732c60:1",
  "hash": "7a284c1860638d56f1cf02bdedbda36250dda23398d91bfa15a16b804253a3ff",
  "cid": "QmV17a284c1860638d56f1cf02bdedbda36250dda233",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291230,
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
      "evaluated_at": 1760291230
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "3d2bea0feb109af2c5c9e15abe85ecb4ceb9c28a7bee51545c0953500d9a70be"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 098545588857560
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 23058630, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285764, 'matching_hash': '7b745f55cd5357b8'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '098545585', 'validation_error': 'Invalid routing number checksum'}}}